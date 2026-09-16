from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_policies_dry_run_create_annotations_error_component import (
        ApiV1PoliciesDryRunCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_archived_at_error_component import (
        ApiV1PoliciesDryRunCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_archived_error_component import (
        ApiV1PoliciesDryRunCreateArchivedErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_archived_reason_error_component import (
        ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_criticality_error_component import (
        ApiV1PoliciesDryRunCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_debug_mode_error_component import (
        ApiV1PoliciesDryRunCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_description_error_component import (
        ApiV1PoliciesDryRunCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_display_name_error_component import (
        ApiV1PoliciesDryRunCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_expression_error_component import (
        ApiV1PoliciesDryRunCreateExpressionErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_kind_error_component import ApiV1PoliciesDryRunCreateKindErrorComponent
    from ..models.api_v1_policies_dry_run_create_kinds_selector_error_component import (
        ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_labels_error_component import (
        ApiV1PoliciesDryRunCreateLabelsErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_metadata_error_component import (
        ApiV1PoliciesDryRunCreateMetadataErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_models_selector_error_component import (
        ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_name_error_component import ApiV1PoliciesDryRunCreateNameErrorComponent
    from ..models.api_v1_policies_dry_run_create_non_field_errors_error_component import (
        ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_order_error_component import (
        ApiV1PoliciesDryRunCreateOrderErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_organizations_selector_error_component import (
        ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_platform_service_error_component import (
        ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_provider_error_component import (
        ApiV1PoliciesDryRunCreateProviderErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_provider_id_error_component import (
        ApiV1PoliciesDryRunCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_provider_reference_error_component import (
        ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_reconciliation_enabled_error_component import (
        ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_sla_availability_error_component import (
        ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_sla_target_error_component import (
        ApiV1PoliciesDryRunCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_slo_availability_error_component import (
        ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_slo_target_error_component import (
        ApiV1PoliciesDryRunCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_target_availability_error_component import (
        ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_tolerations_error_component import (
        ApiV1PoliciesDryRunCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_policies_dry_run_create_workspaces_selector_error_component import (
        ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PoliciesDryRunCreateValidationError")


@_attrs_define
class ApiV1PoliciesDryRunCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PoliciesDryRunCreateAnnotationsErrorComponent |
            ApiV1PoliciesDryRunCreateArchivedAtErrorComponent | ApiV1PoliciesDryRunCreateArchivedErrorComponent |
            ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent | ApiV1PoliciesDryRunCreateCriticalityErrorComponent |
            ApiV1PoliciesDryRunCreateDebugModeErrorComponent | ApiV1PoliciesDryRunCreateDescriptionErrorComponent |
            ApiV1PoliciesDryRunCreateDisplayNameErrorComponent | ApiV1PoliciesDryRunCreateExpressionErrorComponent |
            ApiV1PoliciesDryRunCreateKindErrorComponent | ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent |
            ApiV1PoliciesDryRunCreateLabelsErrorComponent | ApiV1PoliciesDryRunCreateMetadataErrorComponent |
            ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent | ApiV1PoliciesDryRunCreateNameErrorComponent |
            ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent | ApiV1PoliciesDryRunCreateOrderErrorComponent |
            ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent |
            ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent | ApiV1PoliciesDryRunCreateProviderErrorComponent |
            ApiV1PoliciesDryRunCreateProviderIdErrorComponent | ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent |
            ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent |
            ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent | ApiV1PoliciesDryRunCreateSlaTargetErrorComponent |
            ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent | ApiV1PoliciesDryRunCreateSloTargetErrorComponent |
            ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent | ApiV1PoliciesDryRunCreateTolerationsErrorComponent |
            ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PoliciesDryRunCreateAnnotationsErrorComponent
        | ApiV1PoliciesDryRunCreateArchivedAtErrorComponent
        | ApiV1PoliciesDryRunCreateArchivedErrorComponent
        | ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent
        | ApiV1PoliciesDryRunCreateCriticalityErrorComponent
        | ApiV1PoliciesDryRunCreateDebugModeErrorComponent
        | ApiV1PoliciesDryRunCreateDescriptionErrorComponent
        | ApiV1PoliciesDryRunCreateDisplayNameErrorComponent
        | ApiV1PoliciesDryRunCreateExpressionErrorComponent
        | ApiV1PoliciesDryRunCreateKindErrorComponent
        | ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent
        | ApiV1PoliciesDryRunCreateLabelsErrorComponent
        | ApiV1PoliciesDryRunCreateMetadataErrorComponent
        | ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent
        | ApiV1PoliciesDryRunCreateNameErrorComponent
        | ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent
        | ApiV1PoliciesDryRunCreateOrderErrorComponent
        | ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent
        | ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent
        | ApiV1PoliciesDryRunCreateProviderErrorComponent
        | ApiV1PoliciesDryRunCreateProviderIdErrorComponent
        | ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent
        | ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent
        | ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent
        | ApiV1PoliciesDryRunCreateSlaTargetErrorComponent
        | ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent
        | ApiV1PoliciesDryRunCreateSloTargetErrorComponent
        | ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent
        | ApiV1PoliciesDryRunCreateTolerationsErrorComponent
        | ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_policies_dry_run_create_annotations_error_component import (
            ApiV1PoliciesDryRunCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_archived_at_error_component import (
            ApiV1PoliciesDryRunCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_archived_error_component import (
            ApiV1PoliciesDryRunCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_archived_reason_error_component import (
            ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_criticality_error_component import (
            ApiV1PoliciesDryRunCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_debug_mode_error_component import (
            ApiV1PoliciesDryRunCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_description_error_component import (
            ApiV1PoliciesDryRunCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_display_name_error_component import (
            ApiV1PoliciesDryRunCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_expression_error_component import (
            ApiV1PoliciesDryRunCreateExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_kind_error_component import (
            ApiV1PoliciesDryRunCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_kinds_selector_error_component import (
            ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_labels_error_component import (
            ApiV1PoliciesDryRunCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_models_selector_error_component import (
            ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_name_error_component import (
            ApiV1PoliciesDryRunCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_non_field_errors_error_component import (
            ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_order_error_component import (
            ApiV1PoliciesDryRunCreateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_organizations_selector_error_component import (
            ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_platform_service_error_component import (
            ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_provider_error_component import (
            ApiV1PoliciesDryRunCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_provider_id_error_component import (
            ApiV1PoliciesDryRunCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_provider_reference_error_component import (
            ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_reconciliation_enabled_error_component import (
            ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_sla_availability_error_component import (
            ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_sla_target_error_component import (
            ApiV1PoliciesDryRunCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_slo_availability_error_component import (
            ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_slo_target_error_component import (
            ApiV1PoliciesDryRunCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_target_availability_error_component import (
            ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_tolerations_error_component import (
            ApiV1PoliciesDryRunCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_workspaces_selector_error_component import (
            ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_policies_dry_run_create_annotations_error_component import (
            ApiV1PoliciesDryRunCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_archived_at_error_component import (
            ApiV1PoliciesDryRunCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_archived_error_component import (
            ApiV1PoliciesDryRunCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_archived_reason_error_component import (
            ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_criticality_error_component import (
            ApiV1PoliciesDryRunCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_debug_mode_error_component import (
            ApiV1PoliciesDryRunCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_description_error_component import (
            ApiV1PoliciesDryRunCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_display_name_error_component import (
            ApiV1PoliciesDryRunCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_expression_error_component import (
            ApiV1PoliciesDryRunCreateExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_kind_error_component import (
            ApiV1PoliciesDryRunCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_kinds_selector_error_component import (
            ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_labels_error_component import (
            ApiV1PoliciesDryRunCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_metadata_error_component import (
            ApiV1PoliciesDryRunCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_models_selector_error_component import (
            ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_name_error_component import (
            ApiV1PoliciesDryRunCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_non_field_errors_error_component import (
            ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_order_error_component import (
            ApiV1PoliciesDryRunCreateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_organizations_selector_error_component import (
            ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_platform_service_error_component import (
            ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_provider_error_component import (
            ApiV1PoliciesDryRunCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_provider_id_error_component import (
            ApiV1PoliciesDryRunCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_provider_reference_error_component import (
            ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_reconciliation_enabled_error_component import (
            ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_sla_availability_error_component import (
            ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_sla_target_error_component import (
            ApiV1PoliciesDryRunCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_slo_availability_error_component import (
            ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_slo_target_error_component import (
            ApiV1PoliciesDryRunCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_target_availability_error_component import (
            ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_tolerations_error_component import (
            ApiV1PoliciesDryRunCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_dry_run_create_workspaces_selector_error_component import (
            ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PoliciesDryRunCreateAnnotationsErrorComponent
                | ApiV1PoliciesDryRunCreateArchivedAtErrorComponent
                | ApiV1PoliciesDryRunCreateArchivedErrorComponent
                | ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent
                | ApiV1PoliciesDryRunCreateCriticalityErrorComponent
                | ApiV1PoliciesDryRunCreateDebugModeErrorComponent
                | ApiV1PoliciesDryRunCreateDescriptionErrorComponent
                | ApiV1PoliciesDryRunCreateDisplayNameErrorComponent
                | ApiV1PoliciesDryRunCreateExpressionErrorComponent
                | ApiV1PoliciesDryRunCreateKindErrorComponent
                | ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent
                | ApiV1PoliciesDryRunCreateLabelsErrorComponent
                | ApiV1PoliciesDryRunCreateMetadataErrorComponent
                | ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent
                | ApiV1PoliciesDryRunCreateNameErrorComponent
                | ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent
                | ApiV1PoliciesDryRunCreateOrderErrorComponent
                | ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent
                | ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent
                | ApiV1PoliciesDryRunCreateProviderErrorComponent
                | ApiV1PoliciesDryRunCreateProviderIdErrorComponent
                | ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent
                | ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent
                | ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent
                | ApiV1PoliciesDryRunCreateSlaTargetErrorComponent
                | ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent
                | ApiV1PoliciesDryRunCreateSloTargetErrorComponent
                | ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent
                | ApiV1PoliciesDryRunCreateTolerationsErrorComponent
                | ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_0 = (
                        ApiV1PoliciesDryRunCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_1 = (
                        ApiV1PoliciesDryRunCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_2 = (
                        ApiV1PoliciesDryRunCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_3 = (
                        ApiV1PoliciesDryRunCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_4 = (
                        ApiV1PoliciesDryRunCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_5 = (
                        ApiV1PoliciesDryRunCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_6 = (
                        ApiV1PoliciesDryRunCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_7 = (
                        ApiV1PoliciesDryRunCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_8 = (
                        ApiV1PoliciesDryRunCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_9 = (
                        ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_10 = (
                        ApiV1PoliciesDryRunCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_11 = (
                        ApiV1PoliciesDryRunCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_12 = (
                        ApiV1PoliciesDryRunCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_13 = (
                        ApiV1PoliciesDryRunCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_14 = (
                        ApiV1PoliciesDryRunCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_15 = (
                        ApiV1PoliciesDryRunCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_16 = (
                        ApiV1PoliciesDryRunCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_17 = (
                        ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_18 = (
                        ApiV1PoliciesDryRunCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_19 = (
                        ApiV1PoliciesDryRunCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_20 = (
                        ApiV1PoliciesDryRunCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_21 = (
                        ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_22 = (
                        ApiV1PoliciesDryRunCreateExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_23 = (
                        ApiV1PoliciesDryRunCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_24 = (
                        ApiV1PoliciesDryRunCreateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_25 = (
                        ApiV1PoliciesDryRunCreateModelsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_26 = (
                        ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_27 = (
                        ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_dry_run_create_error_type_28 = (
                        ApiV1PoliciesDryRunCreateKindsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_dry_run_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_policies_dry_run_create_error_type_29 = (
                    ApiV1PoliciesDryRunCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_policies_dry_run_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_policies_dry_run_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_policies_dry_run_create_validation_error.additional_properties = d
        return api_v1_policies_dry_run_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

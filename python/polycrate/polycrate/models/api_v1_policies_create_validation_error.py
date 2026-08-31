from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_policies_create_annotations_error_component import ApiV1PoliciesCreateAnnotationsErrorComponent
    from ..models.api_v1_policies_create_archived_at_error_component import ApiV1PoliciesCreateArchivedAtErrorComponent
    from ..models.api_v1_policies_create_archived_error_component import ApiV1PoliciesCreateArchivedErrorComponent
    from ..models.api_v1_policies_create_archived_reason_error_component import (
        ApiV1PoliciesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_policies_create_criticality_error_component import ApiV1PoliciesCreateCriticalityErrorComponent
    from ..models.api_v1_policies_create_debug_mode_error_component import ApiV1PoliciesCreateDebugModeErrorComponent
    from ..models.api_v1_policies_create_description_error_component import ApiV1PoliciesCreateDescriptionErrorComponent
    from ..models.api_v1_policies_create_display_name_error_component import (
        ApiV1PoliciesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_policies_create_expression_error_component import ApiV1PoliciesCreateExpressionErrorComponent
    from ..models.api_v1_policies_create_kind_error_component import ApiV1PoliciesCreateKindErrorComponent
    from ..models.api_v1_policies_create_kinds_selector_error_component import (
        ApiV1PoliciesCreateKindsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_create_labels_error_component import ApiV1PoliciesCreateLabelsErrorComponent
    from ..models.api_v1_policies_create_metadata_error_component import ApiV1PoliciesCreateMetadataErrorComponent
    from ..models.api_v1_policies_create_models_selector_error_component import (
        ApiV1PoliciesCreateModelsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_create_name_error_component import ApiV1PoliciesCreateNameErrorComponent
    from ..models.api_v1_policies_create_non_field_errors_error_component import (
        ApiV1PoliciesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_policies_create_order_error_component import ApiV1PoliciesCreateOrderErrorComponent
    from ..models.api_v1_policies_create_organizations_selector_error_component import (
        ApiV1PoliciesCreateOrganizationsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_create_platform_service_error_component import (
        ApiV1PoliciesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_policies_create_provider_error_component import ApiV1PoliciesCreateProviderErrorComponent
    from ..models.api_v1_policies_create_provider_id_error_component import ApiV1PoliciesCreateProviderIdErrorComponent
    from ..models.api_v1_policies_create_provider_reference_error_component import (
        ApiV1PoliciesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_policies_create_reconciliation_enabled_error_component import (
        ApiV1PoliciesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_policies_create_sla_availability_error_component import (
        ApiV1PoliciesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_create_sla_target_error_component import ApiV1PoliciesCreateSlaTargetErrorComponent
    from ..models.api_v1_policies_create_slo_availability_error_component import (
        ApiV1PoliciesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_create_slo_target_error_component import ApiV1PoliciesCreateSloTargetErrorComponent
    from ..models.api_v1_policies_create_target_availability_error_component import (
        ApiV1PoliciesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_create_tolerations_error_component import ApiV1PoliciesCreateTolerationsErrorComponent
    from ..models.api_v1_policies_create_workspaces_selector_error_component import (
        ApiV1PoliciesCreateWorkspacesSelectorErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PoliciesCreateValidationError")


@_attrs_define
class ApiV1PoliciesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PoliciesCreateAnnotationsErrorComponent | ApiV1PoliciesCreateArchivedAtErrorComponent |
            ApiV1PoliciesCreateArchivedErrorComponent | ApiV1PoliciesCreateArchivedReasonErrorComponent |
            ApiV1PoliciesCreateCriticalityErrorComponent | ApiV1PoliciesCreateDebugModeErrorComponent |
            ApiV1PoliciesCreateDescriptionErrorComponent | ApiV1PoliciesCreateDisplayNameErrorComponent |
            ApiV1PoliciesCreateExpressionErrorComponent | ApiV1PoliciesCreateKindErrorComponent |
            ApiV1PoliciesCreateKindsSelectorErrorComponent | ApiV1PoliciesCreateLabelsErrorComponent |
            ApiV1PoliciesCreateMetadataErrorComponent | ApiV1PoliciesCreateModelsSelectorErrorComponent |
            ApiV1PoliciesCreateNameErrorComponent | ApiV1PoliciesCreateNonFieldErrorsErrorComponent |
            ApiV1PoliciesCreateOrderErrorComponent | ApiV1PoliciesCreateOrganizationsSelectorErrorComponent |
            ApiV1PoliciesCreatePlatformServiceErrorComponent | ApiV1PoliciesCreateProviderErrorComponent |
            ApiV1PoliciesCreateProviderIdErrorComponent | ApiV1PoliciesCreateProviderReferenceErrorComponent |
            ApiV1PoliciesCreateReconciliationEnabledErrorComponent | ApiV1PoliciesCreateSlaAvailabilityErrorComponent |
            ApiV1PoliciesCreateSlaTargetErrorComponent | ApiV1PoliciesCreateSloAvailabilityErrorComponent |
            ApiV1PoliciesCreateSloTargetErrorComponent | ApiV1PoliciesCreateTargetAvailabilityErrorComponent |
            ApiV1PoliciesCreateTolerationsErrorComponent | ApiV1PoliciesCreateWorkspacesSelectorErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PoliciesCreateAnnotationsErrorComponent
        | ApiV1PoliciesCreateArchivedAtErrorComponent
        | ApiV1PoliciesCreateArchivedErrorComponent
        | ApiV1PoliciesCreateArchivedReasonErrorComponent
        | ApiV1PoliciesCreateCriticalityErrorComponent
        | ApiV1PoliciesCreateDebugModeErrorComponent
        | ApiV1PoliciesCreateDescriptionErrorComponent
        | ApiV1PoliciesCreateDisplayNameErrorComponent
        | ApiV1PoliciesCreateExpressionErrorComponent
        | ApiV1PoliciesCreateKindErrorComponent
        | ApiV1PoliciesCreateKindsSelectorErrorComponent
        | ApiV1PoliciesCreateLabelsErrorComponent
        | ApiV1PoliciesCreateMetadataErrorComponent
        | ApiV1PoliciesCreateModelsSelectorErrorComponent
        | ApiV1PoliciesCreateNameErrorComponent
        | ApiV1PoliciesCreateNonFieldErrorsErrorComponent
        | ApiV1PoliciesCreateOrderErrorComponent
        | ApiV1PoliciesCreateOrganizationsSelectorErrorComponent
        | ApiV1PoliciesCreatePlatformServiceErrorComponent
        | ApiV1PoliciesCreateProviderErrorComponent
        | ApiV1PoliciesCreateProviderIdErrorComponent
        | ApiV1PoliciesCreateProviderReferenceErrorComponent
        | ApiV1PoliciesCreateReconciliationEnabledErrorComponent
        | ApiV1PoliciesCreateSlaAvailabilityErrorComponent
        | ApiV1PoliciesCreateSlaTargetErrorComponent
        | ApiV1PoliciesCreateSloAvailabilityErrorComponent
        | ApiV1PoliciesCreateSloTargetErrorComponent
        | ApiV1PoliciesCreateTargetAvailabilityErrorComponent
        | ApiV1PoliciesCreateTolerationsErrorComponent
        | ApiV1PoliciesCreateWorkspacesSelectorErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_policies_create_annotations_error_component import (
            ApiV1PoliciesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_policies_create_archived_at_error_component import (
            ApiV1PoliciesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_policies_create_archived_error_component import ApiV1PoliciesCreateArchivedErrorComponent
        from ..models.api_v1_policies_create_archived_reason_error_component import (
            ApiV1PoliciesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_policies_create_criticality_error_component import (
            ApiV1PoliciesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_policies_create_debug_mode_error_component import (
            ApiV1PoliciesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_policies_create_description_error_component import (
            ApiV1PoliciesCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_policies_create_display_name_error_component import (
            ApiV1PoliciesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_policies_create_expression_error_component import (
            ApiV1PoliciesCreateExpressionErrorComponent,
        )
        from ..models.api_v1_policies_create_kind_error_component import ApiV1PoliciesCreateKindErrorComponent
        from ..models.api_v1_policies_create_kinds_selector_error_component import (
            ApiV1PoliciesCreateKindsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_create_labels_error_component import ApiV1PoliciesCreateLabelsErrorComponent
        from ..models.api_v1_policies_create_models_selector_error_component import (
            ApiV1PoliciesCreateModelsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_create_name_error_component import ApiV1PoliciesCreateNameErrorComponent
        from ..models.api_v1_policies_create_non_field_errors_error_component import (
            ApiV1PoliciesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policies_create_order_error_component import ApiV1PoliciesCreateOrderErrorComponent
        from ..models.api_v1_policies_create_organizations_selector_error_component import (
            ApiV1PoliciesCreateOrganizationsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_create_platform_service_error_component import (
            ApiV1PoliciesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_policies_create_provider_error_component import ApiV1PoliciesCreateProviderErrorComponent
        from ..models.api_v1_policies_create_provider_id_error_component import (
            ApiV1PoliciesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_policies_create_provider_reference_error_component import (
            ApiV1PoliciesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_policies_create_reconciliation_enabled_error_component import (
            ApiV1PoliciesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_policies_create_sla_availability_error_component import (
            ApiV1PoliciesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_create_sla_target_error_component import (
            ApiV1PoliciesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_policies_create_slo_availability_error_component import (
            ApiV1PoliciesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_create_slo_target_error_component import (
            ApiV1PoliciesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_policies_create_target_availability_error_component import (
            ApiV1PoliciesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_create_tolerations_error_component import (
            ApiV1PoliciesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_policies_create_workspaces_selector_error_component import (
            ApiV1PoliciesCreateWorkspacesSelectorErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PoliciesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateModelsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateOrganizationsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateWorkspacesSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesCreateKindsSelectorErrorComponent):
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
        from ..models.api_v1_policies_create_annotations_error_component import (
            ApiV1PoliciesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_policies_create_archived_at_error_component import (
            ApiV1PoliciesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_policies_create_archived_error_component import ApiV1PoliciesCreateArchivedErrorComponent
        from ..models.api_v1_policies_create_archived_reason_error_component import (
            ApiV1PoliciesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_policies_create_criticality_error_component import (
            ApiV1PoliciesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_policies_create_debug_mode_error_component import (
            ApiV1PoliciesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_policies_create_description_error_component import (
            ApiV1PoliciesCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_policies_create_display_name_error_component import (
            ApiV1PoliciesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_policies_create_expression_error_component import (
            ApiV1PoliciesCreateExpressionErrorComponent,
        )
        from ..models.api_v1_policies_create_kind_error_component import ApiV1PoliciesCreateKindErrorComponent
        from ..models.api_v1_policies_create_kinds_selector_error_component import (
            ApiV1PoliciesCreateKindsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_create_labels_error_component import ApiV1PoliciesCreateLabelsErrorComponent
        from ..models.api_v1_policies_create_metadata_error_component import ApiV1PoliciesCreateMetadataErrorComponent
        from ..models.api_v1_policies_create_models_selector_error_component import (
            ApiV1PoliciesCreateModelsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_create_name_error_component import ApiV1PoliciesCreateNameErrorComponent
        from ..models.api_v1_policies_create_non_field_errors_error_component import (
            ApiV1PoliciesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policies_create_order_error_component import ApiV1PoliciesCreateOrderErrorComponent
        from ..models.api_v1_policies_create_organizations_selector_error_component import (
            ApiV1PoliciesCreateOrganizationsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_create_platform_service_error_component import (
            ApiV1PoliciesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_policies_create_provider_error_component import ApiV1PoliciesCreateProviderErrorComponent
        from ..models.api_v1_policies_create_provider_id_error_component import (
            ApiV1PoliciesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_policies_create_provider_reference_error_component import (
            ApiV1PoliciesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_policies_create_reconciliation_enabled_error_component import (
            ApiV1PoliciesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_policies_create_sla_availability_error_component import (
            ApiV1PoliciesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_create_sla_target_error_component import (
            ApiV1PoliciesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_policies_create_slo_availability_error_component import (
            ApiV1PoliciesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_create_slo_target_error_component import (
            ApiV1PoliciesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_policies_create_target_availability_error_component import (
            ApiV1PoliciesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_create_tolerations_error_component import (
            ApiV1PoliciesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_policies_create_workspaces_selector_error_component import (
            ApiV1PoliciesCreateWorkspacesSelectorErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PoliciesCreateAnnotationsErrorComponent
                | ApiV1PoliciesCreateArchivedAtErrorComponent
                | ApiV1PoliciesCreateArchivedErrorComponent
                | ApiV1PoliciesCreateArchivedReasonErrorComponent
                | ApiV1PoliciesCreateCriticalityErrorComponent
                | ApiV1PoliciesCreateDebugModeErrorComponent
                | ApiV1PoliciesCreateDescriptionErrorComponent
                | ApiV1PoliciesCreateDisplayNameErrorComponent
                | ApiV1PoliciesCreateExpressionErrorComponent
                | ApiV1PoliciesCreateKindErrorComponent
                | ApiV1PoliciesCreateKindsSelectorErrorComponent
                | ApiV1PoliciesCreateLabelsErrorComponent
                | ApiV1PoliciesCreateMetadataErrorComponent
                | ApiV1PoliciesCreateModelsSelectorErrorComponent
                | ApiV1PoliciesCreateNameErrorComponent
                | ApiV1PoliciesCreateNonFieldErrorsErrorComponent
                | ApiV1PoliciesCreateOrderErrorComponent
                | ApiV1PoliciesCreateOrganizationsSelectorErrorComponent
                | ApiV1PoliciesCreatePlatformServiceErrorComponent
                | ApiV1PoliciesCreateProviderErrorComponent
                | ApiV1PoliciesCreateProviderIdErrorComponent
                | ApiV1PoliciesCreateProviderReferenceErrorComponent
                | ApiV1PoliciesCreateReconciliationEnabledErrorComponent
                | ApiV1PoliciesCreateSlaAvailabilityErrorComponent
                | ApiV1PoliciesCreateSlaTargetErrorComponent
                | ApiV1PoliciesCreateSloAvailabilityErrorComponent
                | ApiV1PoliciesCreateSloTargetErrorComponent
                | ApiV1PoliciesCreateTargetAvailabilityErrorComponent
                | ApiV1PoliciesCreateTolerationsErrorComponent
                | ApiV1PoliciesCreateWorkspacesSelectorErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_0 = (
                        ApiV1PoliciesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_1 = (
                        ApiV1PoliciesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_2 = (
                        ApiV1PoliciesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_3 = (
                        ApiV1PoliciesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_4 = (
                        ApiV1PoliciesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_5 = (
                        ApiV1PoliciesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_6 = (
                        ApiV1PoliciesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_7 = (
                        ApiV1PoliciesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_8 = (
                        ApiV1PoliciesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_9 = (
                        ApiV1PoliciesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_10 = (
                        ApiV1PoliciesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_11 = (
                        ApiV1PoliciesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_12 = (
                        ApiV1PoliciesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_13 = (
                        ApiV1PoliciesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_14 = (
                        ApiV1PoliciesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_15 = (
                        ApiV1PoliciesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_16 = (
                        ApiV1PoliciesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_17 = (
                        ApiV1PoliciesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_18 = (
                        ApiV1PoliciesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_19 = (
                        ApiV1PoliciesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_20 = (
                        ApiV1PoliciesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_21 = (
                        ApiV1PoliciesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_22 = (
                        ApiV1PoliciesCreateExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_23 = (
                        ApiV1PoliciesCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_24 = (
                        ApiV1PoliciesCreateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_25 = (
                        ApiV1PoliciesCreateModelsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_26 = (
                        ApiV1PoliciesCreateOrganizationsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_27 = (
                        ApiV1PoliciesCreateWorkspacesSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_create_error_type_28 = (
                        ApiV1PoliciesCreateKindsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_policies_create_error_type_29 = (
                    ApiV1PoliciesCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_policies_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_policies_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_policies_create_validation_error.additional_properties = d
        return api_v1_policies_create_validation_error

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

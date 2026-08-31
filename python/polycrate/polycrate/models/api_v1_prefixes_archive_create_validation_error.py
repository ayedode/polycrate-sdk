from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_prefixes_archive_create_annotations_error_component import (
        ApiV1PrefixesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_archived_at_error_component import (
        ApiV1PrefixesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_archived_error_component import (
        ApiV1PrefixesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_archived_reason_error_component import (
        ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_credential_id_error_component import (
        ApiV1PrefixesArchiveCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_criticality_error_component import (
        ApiV1PrefixesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_debug_mode_error_component import (
        ApiV1PrefixesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_description_error_component import (
        ApiV1PrefixesArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_display_name_error_component import (
        ApiV1PrefixesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_kind_error_component import (
        ApiV1PrefixesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_labels_error_component import (
        ApiV1PrefixesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_name_error_component import (
        ApiV1PrefixesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_non_field_errors_error_component import (
        ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_organization_id_error_component import (
        ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_platform_service_error_component import (
        ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_provider_entity_id_error_component import (
        ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_provider_error_component import (
        ApiV1PrefixesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_provider_id_error_component import (
        ApiV1PrefixesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_provider_reference_error_component import (
        ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_purpose_error_component import (
        ApiV1PrefixesArchiveCreatePurposeErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_reconciliation_enabled_error_component import (
        ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_region_id_error_component import (
        ApiV1PrefixesArchiveCreateRegionIdErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_sla_availability_error_component import (
        ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_sla_target_error_component import (
        ApiV1PrefixesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_slo_availability_error_component import (
        ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_slo_target_error_component import (
        ApiV1PrefixesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_target_availability_error_component import (
        ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_tolerations_error_component import (
        ApiV1PrefixesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_prefixes_archive_create_workspace_id_error_component import (
        ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PrefixesArchiveCreateValidationError")


@_attrs_define
class ApiV1PrefixesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PrefixesArchiveCreateAnnotationsErrorComponent |
            ApiV1PrefixesArchiveCreateArchivedAtErrorComponent | ApiV1PrefixesArchiveCreateArchivedErrorComponent |
            ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent | ApiV1PrefixesArchiveCreateCredentialIdErrorComponent |
            ApiV1PrefixesArchiveCreateCriticalityErrorComponent | ApiV1PrefixesArchiveCreateDebugModeErrorComponent |
            ApiV1PrefixesArchiveCreateDescriptionErrorComponent | ApiV1PrefixesArchiveCreateDisplayNameErrorComponent |
            ApiV1PrefixesArchiveCreateKindErrorComponent | ApiV1PrefixesArchiveCreateLabelsErrorComponent |
            ApiV1PrefixesArchiveCreateNameErrorComponent | ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent | ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent
            | ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent | ApiV1PrefixesArchiveCreateProviderErrorComponent |
            ApiV1PrefixesArchiveCreateProviderIdErrorComponent | ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent |
            ApiV1PrefixesArchiveCreatePurposeErrorComponent | ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent
            | ApiV1PrefixesArchiveCreateRegionIdErrorComponent | ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PrefixesArchiveCreateSlaTargetErrorComponent | ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PrefixesArchiveCreateSloTargetErrorComponent | ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PrefixesArchiveCreateTolerationsErrorComponent | ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PrefixesArchiveCreateAnnotationsErrorComponent
        | ApiV1PrefixesArchiveCreateArchivedAtErrorComponent
        | ApiV1PrefixesArchiveCreateArchivedErrorComponent
        | ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent
        | ApiV1PrefixesArchiveCreateCredentialIdErrorComponent
        | ApiV1PrefixesArchiveCreateCriticalityErrorComponent
        | ApiV1PrefixesArchiveCreateDebugModeErrorComponent
        | ApiV1PrefixesArchiveCreateDescriptionErrorComponent
        | ApiV1PrefixesArchiveCreateDisplayNameErrorComponent
        | ApiV1PrefixesArchiveCreateKindErrorComponent
        | ApiV1PrefixesArchiveCreateLabelsErrorComponent
        | ApiV1PrefixesArchiveCreateNameErrorComponent
        | ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent
        | ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent
        | ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent
        | ApiV1PrefixesArchiveCreateProviderErrorComponent
        | ApiV1PrefixesArchiveCreateProviderIdErrorComponent
        | ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent
        | ApiV1PrefixesArchiveCreatePurposeErrorComponent
        | ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PrefixesArchiveCreateRegionIdErrorComponent
        | ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PrefixesArchiveCreateSlaTargetErrorComponent
        | ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PrefixesArchiveCreateSloTargetErrorComponent
        | ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PrefixesArchiveCreateTolerationsErrorComponent
        | ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_prefixes_archive_create_annotations_error_component import (
            ApiV1PrefixesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_archived_at_error_component import (
            ApiV1PrefixesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_archived_error_component import (
            ApiV1PrefixesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_archived_reason_error_component import (
            ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_credential_id_error_component import (
            ApiV1PrefixesArchiveCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_criticality_error_component import (
            ApiV1PrefixesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_debug_mode_error_component import (
            ApiV1PrefixesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_display_name_error_component import (
            ApiV1PrefixesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_kind_error_component import (
            ApiV1PrefixesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_labels_error_component import (
            ApiV1PrefixesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_name_error_component import (
            ApiV1PrefixesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_non_field_errors_error_component import (
            ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_organization_id_error_component import (
            ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_platform_service_error_component import (
            ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_entity_id_error_component import (
            ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_error_component import (
            ApiV1PrefixesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_id_error_component import (
            ApiV1PrefixesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_reference_error_component import (
            ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_purpose_error_component import (
            ApiV1PrefixesArchiveCreatePurposeErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_reconciliation_enabled_error_component import (
            ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_region_id_error_component import (
            ApiV1PrefixesArchiveCreateRegionIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_sla_availability_error_component import (
            ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_sla_target_error_component import (
            ApiV1PrefixesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_slo_availability_error_component import (
            ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_slo_target_error_component import (
            ApiV1PrefixesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_target_availability_error_component import (
            ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_tolerations_error_component import (
            ApiV1PrefixesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_workspace_id_error_component import (
            ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateRegionIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesArchiveCreatePurposeErrorComponent):
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
        from ..models.api_v1_prefixes_archive_create_annotations_error_component import (
            ApiV1PrefixesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_archived_at_error_component import (
            ApiV1PrefixesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_archived_error_component import (
            ApiV1PrefixesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_archived_reason_error_component import (
            ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_credential_id_error_component import (
            ApiV1PrefixesArchiveCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_criticality_error_component import (
            ApiV1PrefixesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_debug_mode_error_component import (
            ApiV1PrefixesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_description_error_component import (
            ApiV1PrefixesArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_display_name_error_component import (
            ApiV1PrefixesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_kind_error_component import (
            ApiV1PrefixesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_labels_error_component import (
            ApiV1PrefixesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_name_error_component import (
            ApiV1PrefixesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_non_field_errors_error_component import (
            ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_organization_id_error_component import (
            ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_platform_service_error_component import (
            ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_entity_id_error_component import (
            ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_error_component import (
            ApiV1PrefixesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_id_error_component import (
            ApiV1PrefixesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_provider_reference_error_component import (
            ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_purpose_error_component import (
            ApiV1PrefixesArchiveCreatePurposeErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_reconciliation_enabled_error_component import (
            ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_region_id_error_component import (
            ApiV1PrefixesArchiveCreateRegionIdErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_sla_availability_error_component import (
            ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_sla_target_error_component import (
            ApiV1PrefixesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_slo_availability_error_component import (
            ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_slo_target_error_component import (
            ApiV1PrefixesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_target_availability_error_component import (
            ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_tolerations_error_component import (
            ApiV1PrefixesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_prefixes_archive_create_workspace_id_error_component import (
            ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PrefixesArchiveCreateAnnotationsErrorComponent
                | ApiV1PrefixesArchiveCreateArchivedAtErrorComponent
                | ApiV1PrefixesArchiveCreateArchivedErrorComponent
                | ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent
                | ApiV1PrefixesArchiveCreateCredentialIdErrorComponent
                | ApiV1PrefixesArchiveCreateCriticalityErrorComponent
                | ApiV1PrefixesArchiveCreateDebugModeErrorComponent
                | ApiV1PrefixesArchiveCreateDescriptionErrorComponent
                | ApiV1PrefixesArchiveCreateDisplayNameErrorComponent
                | ApiV1PrefixesArchiveCreateKindErrorComponent
                | ApiV1PrefixesArchiveCreateLabelsErrorComponent
                | ApiV1PrefixesArchiveCreateNameErrorComponent
                | ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent
                | ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent
                | ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent
                | ApiV1PrefixesArchiveCreateProviderErrorComponent
                | ApiV1PrefixesArchiveCreateProviderIdErrorComponent
                | ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent
                | ApiV1PrefixesArchiveCreatePurposeErrorComponent
                | ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PrefixesArchiveCreateRegionIdErrorComponent
                | ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PrefixesArchiveCreateSlaTargetErrorComponent
                | ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PrefixesArchiveCreateSloTargetErrorComponent
                | ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PrefixesArchiveCreateTolerationsErrorComponent
                | ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_0 = (
                        ApiV1PrefixesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_1 = (
                        ApiV1PrefixesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_2 = (
                        ApiV1PrefixesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_3 = (
                        ApiV1PrefixesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_4 = (
                        ApiV1PrefixesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_5 = (
                        ApiV1PrefixesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_6 = (
                        ApiV1PrefixesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_7 = (
                        ApiV1PrefixesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_8 = (
                        ApiV1PrefixesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_9 = (
                        ApiV1PrefixesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_10 = (
                        ApiV1PrefixesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_11 = (
                        ApiV1PrefixesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_12 = (
                        ApiV1PrefixesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_13 = (
                        ApiV1PrefixesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_14 = (
                        ApiV1PrefixesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_15 = (
                        ApiV1PrefixesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_16 = (
                        ApiV1PrefixesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_17 = (
                        ApiV1PrefixesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_18 = (
                        ApiV1PrefixesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_19 = (
                        ApiV1PrefixesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_20 = (
                        ApiV1PrefixesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_21 = (
                        ApiV1PrefixesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_22 = (
                        ApiV1PrefixesArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_23 = (
                        ApiV1PrefixesArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_24 = (
                        ApiV1PrefixesArchiveCreateRegionIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_25 = (
                        ApiV1PrefixesArchiveCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_26 = (
                        ApiV1PrefixesArchiveCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_archive_create_error_type_27 = (
                        ApiV1PrefixesArchiveCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_prefixes_archive_create_error_type_28 = (
                    ApiV1PrefixesArchiveCreateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_prefixes_archive_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_prefixes_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_prefixes_archive_create_validation_error.additional_properties = d
        return api_v1_prefixes_archive_create_validation_error

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

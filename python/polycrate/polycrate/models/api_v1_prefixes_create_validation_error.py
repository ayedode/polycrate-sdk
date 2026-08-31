from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_prefixes_create_annotations_error_component import ApiV1PrefixesCreateAnnotationsErrorComponent
    from ..models.api_v1_prefixes_create_archived_at_error_component import ApiV1PrefixesCreateArchivedAtErrorComponent
    from ..models.api_v1_prefixes_create_archived_error_component import ApiV1PrefixesCreateArchivedErrorComponent
    from ..models.api_v1_prefixes_create_archived_reason_error_component import (
        ApiV1PrefixesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_prefixes_create_credential_id_error_component import (
        ApiV1PrefixesCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_prefixes_create_criticality_error_component import ApiV1PrefixesCreateCriticalityErrorComponent
    from ..models.api_v1_prefixes_create_debug_mode_error_component import ApiV1PrefixesCreateDebugModeErrorComponent
    from ..models.api_v1_prefixes_create_description_error_component import ApiV1PrefixesCreateDescriptionErrorComponent
    from ..models.api_v1_prefixes_create_display_name_error_component import (
        ApiV1PrefixesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_prefixes_create_kind_error_component import ApiV1PrefixesCreateKindErrorComponent
    from ..models.api_v1_prefixes_create_labels_error_component import ApiV1PrefixesCreateLabelsErrorComponent
    from ..models.api_v1_prefixes_create_name_error_component import ApiV1PrefixesCreateNameErrorComponent
    from ..models.api_v1_prefixes_create_non_field_errors_error_component import (
        ApiV1PrefixesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_prefixes_create_organization_id_error_component import (
        ApiV1PrefixesCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_prefixes_create_platform_service_error_component import (
        ApiV1PrefixesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_prefixes_create_provider_entity_id_error_component import (
        ApiV1PrefixesCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_prefixes_create_provider_error_component import ApiV1PrefixesCreateProviderErrorComponent
    from ..models.api_v1_prefixes_create_provider_id_error_component import ApiV1PrefixesCreateProviderIdErrorComponent
    from ..models.api_v1_prefixes_create_provider_reference_error_component import (
        ApiV1PrefixesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_prefixes_create_purpose_error_component import ApiV1PrefixesCreatePurposeErrorComponent
    from ..models.api_v1_prefixes_create_reconciliation_enabled_error_component import (
        ApiV1PrefixesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_prefixes_create_region_id_error_component import ApiV1PrefixesCreateRegionIdErrorComponent
    from ..models.api_v1_prefixes_create_sla_availability_error_component import (
        ApiV1PrefixesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_create_sla_target_error_component import ApiV1PrefixesCreateSlaTargetErrorComponent
    from ..models.api_v1_prefixes_create_slo_availability_error_component import (
        ApiV1PrefixesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_create_slo_target_error_component import ApiV1PrefixesCreateSloTargetErrorComponent
    from ..models.api_v1_prefixes_create_target_availability_error_component import (
        ApiV1PrefixesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_create_tolerations_error_component import ApiV1PrefixesCreateTolerationsErrorComponent
    from ..models.api_v1_prefixes_create_workspace_id_error_component import (
        ApiV1PrefixesCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PrefixesCreateValidationError")


@_attrs_define
class ApiV1PrefixesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PrefixesCreateAnnotationsErrorComponent | ApiV1PrefixesCreateArchivedAtErrorComponent |
            ApiV1PrefixesCreateArchivedErrorComponent | ApiV1PrefixesCreateArchivedReasonErrorComponent |
            ApiV1PrefixesCreateCredentialIdErrorComponent | ApiV1PrefixesCreateCriticalityErrorComponent |
            ApiV1PrefixesCreateDebugModeErrorComponent | ApiV1PrefixesCreateDescriptionErrorComponent |
            ApiV1PrefixesCreateDisplayNameErrorComponent | ApiV1PrefixesCreateKindErrorComponent |
            ApiV1PrefixesCreateLabelsErrorComponent | ApiV1PrefixesCreateNameErrorComponent |
            ApiV1PrefixesCreateNonFieldErrorsErrorComponent | ApiV1PrefixesCreateOrganizationIdErrorComponent |
            ApiV1PrefixesCreatePlatformServiceErrorComponent | ApiV1PrefixesCreateProviderEntityIdErrorComponent |
            ApiV1PrefixesCreateProviderErrorComponent | ApiV1PrefixesCreateProviderIdErrorComponent |
            ApiV1PrefixesCreateProviderReferenceErrorComponent | ApiV1PrefixesCreatePurposeErrorComponent |
            ApiV1PrefixesCreateReconciliationEnabledErrorComponent | ApiV1PrefixesCreateRegionIdErrorComponent |
            ApiV1PrefixesCreateSlaAvailabilityErrorComponent | ApiV1PrefixesCreateSlaTargetErrorComponent |
            ApiV1PrefixesCreateSloAvailabilityErrorComponent | ApiV1PrefixesCreateSloTargetErrorComponent |
            ApiV1PrefixesCreateTargetAvailabilityErrorComponent | ApiV1PrefixesCreateTolerationsErrorComponent |
            ApiV1PrefixesCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PrefixesCreateAnnotationsErrorComponent
        | ApiV1PrefixesCreateArchivedAtErrorComponent
        | ApiV1PrefixesCreateArchivedErrorComponent
        | ApiV1PrefixesCreateArchivedReasonErrorComponent
        | ApiV1PrefixesCreateCredentialIdErrorComponent
        | ApiV1PrefixesCreateCriticalityErrorComponent
        | ApiV1PrefixesCreateDebugModeErrorComponent
        | ApiV1PrefixesCreateDescriptionErrorComponent
        | ApiV1PrefixesCreateDisplayNameErrorComponent
        | ApiV1PrefixesCreateKindErrorComponent
        | ApiV1PrefixesCreateLabelsErrorComponent
        | ApiV1PrefixesCreateNameErrorComponent
        | ApiV1PrefixesCreateNonFieldErrorsErrorComponent
        | ApiV1PrefixesCreateOrganizationIdErrorComponent
        | ApiV1PrefixesCreatePlatformServiceErrorComponent
        | ApiV1PrefixesCreateProviderEntityIdErrorComponent
        | ApiV1PrefixesCreateProviderErrorComponent
        | ApiV1PrefixesCreateProviderIdErrorComponent
        | ApiV1PrefixesCreateProviderReferenceErrorComponent
        | ApiV1PrefixesCreatePurposeErrorComponent
        | ApiV1PrefixesCreateReconciliationEnabledErrorComponent
        | ApiV1PrefixesCreateRegionIdErrorComponent
        | ApiV1PrefixesCreateSlaAvailabilityErrorComponent
        | ApiV1PrefixesCreateSlaTargetErrorComponent
        | ApiV1PrefixesCreateSloAvailabilityErrorComponent
        | ApiV1PrefixesCreateSloTargetErrorComponent
        | ApiV1PrefixesCreateTargetAvailabilityErrorComponent
        | ApiV1PrefixesCreateTolerationsErrorComponent
        | ApiV1PrefixesCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_prefixes_create_annotations_error_component import (
            ApiV1PrefixesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_prefixes_create_archived_at_error_component import (
            ApiV1PrefixesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_prefixes_create_archived_error_component import ApiV1PrefixesCreateArchivedErrorComponent
        from ..models.api_v1_prefixes_create_archived_reason_error_component import (
            ApiV1PrefixesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_prefixes_create_credential_id_error_component import (
            ApiV1PrefixesCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_criticality_error_component import (
            ApiV1PrefixesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_debug_mode_error_component import (
            ApiV1PrefixesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_prefixes_create_display_name_error_component import (
            ApiV1PrefixesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_prefixes_create_kind_error_component import ApiV1PrefixesCreateKindErrorComponent
        from ..models.api_v1_prefixes_create_labels_error_component import ApiV1PrefixesCreateLabelsErrorComponent
        from ..models.api_v1_prefixes_create_name_error_component import ApiV1PrefixesCreateNameErrorComponent
        from ..models.api_v1_prefixes_create_non_field_errors_error_component import (
            ApiV1PrefixesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_prefixes_create_organization_id_error_component import (
            ApiV1PrefixesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_platform_service_error_component import (
            ApiV1PrefixesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_prefixes_create_provider_entity_id_error_component import (
            ApiV1PrefixesCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_provider_error_component import ApiV1PrefixesCreateProviderErrorComponent
        from ..models.api_v1_prefixes_create_provider_id_error_component import (
            ApiV1PrefixesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_provider_reference_error_component import (
            ApiV1PrefixesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_prefixes_create_purpose_error_component import ApiV1PrefixesCreatePurposeErrorComponent
        from ..models.api_v1_prefixes_create_reconciliation_enabled_error_component import (
            ApiV1PrefixesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_prefixes_create_region_id_error_component import ApiV1PrefixesCreateRegionIdErrorComponent
        from ..models.api_v1_prefixes_create_sla_availability_error_component import (
            ApiV1PrefixesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_sla_target_error_component import (
            ApiV1PrefixesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_create_slo_availability_error_component import (
            ApiV1PrefixesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_slo_target_error_component import (
            ApiV1PrefixesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_create_target_availability_error_component import (
            ApiV1PrefixesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_tolerations_error_component import (
            ApiV1PrefixesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_prefixes_create_workspace_id_error_component import (
            ApiV1PrefixesCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PrefixesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateRegionIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesCreatePurposeErrorComponent):
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
        from ..models.api_v1_prefixes_create_annotations_error_component import (
            ApiV1PrefixesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_prefixes_create_archived_at_error_component import (
            ApiV1PrefixesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_prefixes_create_archived_error_component import ApiV1PrefixesCreateArchivedErrorComponent
        from ..models.api_v1_prefixes_create_archived_reason_error_component import (
            ApiV1PrefixesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_prefixes_create_credential_id_error_component import (
            ApiV1PrefixesCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_criticality_error_component import (
            ApiV1PrefixesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_debug_mode_error_component import (
            ApiV1PrefixesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_prefixes_create_description_error_component import (
            ApiV1PrefixesCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_prefixes_create_display_name_error_component import (
            ApiV1PrefixesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_prefixes_create_kind_error_component import ApiV1PrefixesCreateKindErrorComponent
        from ..models.api_v1_prefixes_create_labels_error_component import ApiV1PrefixesCreateLabelsErrorComponent
        from ..models.api_v1_prefixes_create_name_error_component import ApiV1PrefixesCreateNameErrorComponent
        from ..models.api_v1_prefixes_create_non_field_errors_error_component import (
            ApiV1PrefixesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_prefixes_create_organization_id_error_component import (
            ApiV1PrefixesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_platform_service_error_component import (
            ApiV1PrefixesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_prefixes_create_provider_entity_id_error_component import (
            ApiV1PrefixesCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_provider_error_component import ApiV1PrefixesCreateProviderErrorComponent
        from ..models.api_v1_prefixes_create_provider_id_error_component import (
            ApiV1PrefixesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_prefixes_create_provider_reference_error_component import (
            ApiV1PrefixesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_prefixes_create_purpose_error_component import ApiV1PrefixesCreatePurposeErrorComponent
        from ..models.api_v1_prefixes_create_reconciliation_enabled_error_component import (
            ApiV1PrefixesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_prefixes_create_region_id_error_component import ApiV1PrefixesCreateRegionIdErrorComponent
        from ..models.api_v1_prefixes_create_sla_availability_error_component import (
            ApiV1PrefixesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_sla_target_error_component import (
            ApiV1PrefixesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_create_slo_availability_error_component import (
            ApiV1PrefixesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_slo_target_error_component import (
            ApiV1PrefixesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_create_target_availability_error_component import (
            ApiV1PrefixesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_create_tolerations_error_component import (
            ApiV1PrefixesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_prefixes_create_workspace_id_error_component import (
            ApiV1PrefixesCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PrefixesCreateAnnotationsErrorComponent
                | ApiV1PrefixesCreateArchivedAtErrorComponent
                | ApiV1PrefixesCreateArchivedErrorComponent
                | ApiV1PrefixesCreateArchivedReasonErrorComponent
                | ApiV1PrefixesCreateCredentialIdErrorComponent
                | ApiV1PrefixesCreateCriticalityErrorComponent
                | ApiV1PrefixesCreateDebugModeErrorComponent
                | ApiV1PrefixesCreateDescriptionErrorComponent
                | ApiV1PrefixesCreateDisplayNameErrorComponent
                | ApiV1PrefixesCreateKindErrorComponent
                | ApiV1PrefixesCreateLabelsErrorComponent
                | ApiV1PrefixesCreateNameErrorComponent
                | ApiV1PrefixesCreateNonFieldErrorsErrorComponent
                | ApiV1PrefixesCreateOrganizationIdErrorComponent
                | ApiV1PrefixesCreatePlatformServiceErrorComponent
                | ApiV1PrefixesCreateProviderEntityIdErrorComponent
                | ApiV1PrefixesCreateProviderErrorComponent
                | ApiV1PrefixesCreateProviderIdErrorComponent
                | ApiV1PrefixesCreateProviderReferenceErrorComponent
                | ApiV1PrefixesCreatePurposeErrorComponent
                | ApiV1PrefixesCreateReconciliationEnabledErrorComponent
                | ApiV1PrefixesCreateRegionIdErrorComponent
                | ApiV1PrefixesCreateSlaAvailabilityErrorComponent
                | ApiV1PrefixesCreateSlaTargetErrorComponent
                | ApiV1PrefixesCreateSloAvailabilityErrorComponent
                | ApiV1PrefixesCreateSloTargetErrorComponent
                | ApiV1PrefixesCreateTargetAvailabilityErrorComponent
                | ApiV1PrefixesCreateTolerationsErrorComponent
                | ApiV1PrefixesCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_0 = (
                        ApiV1PrefixesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_1 = (
                        ApiV1PrefixesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_2 = (
                        ApiV1PrefixesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_3 = (
                        ApiV1PrefixesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_4 = (
                        ApiV1PrefixesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_5 = (
                        ApiV1PrefixesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_6 = (
                        ApiV1PrefixesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_7 = (
                        ApiV1PrefixesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_8 = (
                        ApiV1PrefixesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_9 = (
                        ApiV1PrefixesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_10 = (
                        ApiV1PrefixesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_11 = (
                        ApiV1PrefixesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_12 = (
                        ApiV1PrefixesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_13 = (
                        ApiV1PrefixesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_14 = (
                        ApiV1PrefixesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_15 = (
                        ApiV1PrefixesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_16 = (
                        ApiV1PrefixesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_17 = (
                        ApiV1PrefixesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_18 = (
                        ApiV1PrefixesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_19 = (
                        ApiV1PrefixesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_20 = (
                        ApiV1PrefixesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_21 = (
                        ApiV1PrefixesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_22 = (
                        ApiV1PrefixesCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_23 = (
                        ApiV1PrefixesCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_24 = (
                        ApiV1PrefixesCreateRegionIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_25 = (
                        ApiV1PrefixesCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_26 = (
                        ApiV1PrefixesCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_create_error_type_27 = (
                        ApiV1PrefixesCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_prefixes_create_error_type_28 = (
                    ApiV1PrefixesCreateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_prefixes_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_prefixes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_prefixes_create_validation_error.additional_properties = d
        return api_v1_prefixes_create_validation_error

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

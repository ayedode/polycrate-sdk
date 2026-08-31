from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_prefixes_update_annotations_error_component import ApiV1PrefixesUpdateAnnotationsErrorComponent
    from ..models.api_v1_prefixes_update_archived_at_error_component import ApiV1PrefixesUpdateArchivedAtErrorComponent
    from ..models.api_v1_prefixes_update_archived_error_component import ApiV1PrefixesUpdateArchivedErrorComponent
    from ..models.api_v1_prefixes_update_archived_reason_error_component import (
        ApiV1PrefixesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_prefixes_update_credential_id_error_component import (
        ApiV1PrefixesUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_prefixes_update_criticality_error_component import ApiV1PrefixesUpdateCriticalityErrorComponent
    from ..models.api_v1_prefixes_update_debug_mode_error_component import ApiV1PrefixesUpdateDebugModeErrorComponent
    from ..models.api_v1_prefixes_update_description_error_component import ApiV1PrefixesUpdateDescriptionErrorComponent
    from ..models.api_v1_prefixes_update_display_name_error_component import (
        ApiV1PrefixesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_prefixes_update_kind_error_component import ApiV1PrefixesUpdateKindErrorComponent
    from ..models.api_v1_prefixes_update_labels_error_component import ApiV1PrefixesUpdateLabelsErrorComponent
    from ..models.api_v1_prefixes_update_name_error_component import ApiV1PrefixesUpdateNameErrorComponent
    from ..models.api_v1_prefixes_update_non_field_errors_error_component import (
        ApiV1PrefixesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_prefixes_update_organization_id_error_component import (
        ApiV1PrefixesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_prefixes_update_platform_service_error_component import (
        ApiV1PrefixesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_prefixes_update_provider_entity_id_error_component import (
        ApiV1PrefixesUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_prefixes_update_provider_error_component import ApiV1PrefixesUpdateProviderErrorComponent
    from ..models.api_v1_prefixes_update_provider_id_error_component import ApiV1PrefixesUpdateProviderIdErrorComponent
    from ..models.api_v1_prefixes_update_provider_reference_error_component import (
        ApiV1PrefixesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_prefixes_update_purpose_error_component import ApiV1PrefixesUpdatePurposeErrorComponent
    from ..models.api_v1_prefixes_update_reconciliation_enabled_error_component import (
        ApiV1PrefixesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_prefixes_update_region_id_error_component import ApiV1PrefixesUpdateRegionIdErrorComponent
    from ..models.api_v1_prefixes_update_sla_availability_error_component import (
        ApiV1PrefixesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_update_sla_target_error_component import ApiV1PrefixesUpdateSlaTargetErrorComponent
    from ..models.api_v1_prefixes_update_slo_availability_error_component import (
        ApiV1PrefixesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_update_slo_target_error_component import ApiV1PrefixesUpdateSloTargetErrorComponent
    from ..models.api_v1_prefixes_update_target_availability_error_component import (
        ApiV1PrefixesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_update_tolerations_error_component import ApiV1PrefixesUpdateTolerationsErrorComponent
    from ..models.api_v1_prefixes_update_workspace_id_error_component import (
        ApiV1PrefixesUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PrefixesUpdateValidationError")


@_attrs_define
class ApiV1PrefixesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PrefixesUpdateAnnotationsErrorComponent | ApiV1PrefixesUpdateArchivedAtErrorComponent |
            ApiV1PrefixesUpdateArchivedErrorComponent | ApiV1PrefixesUpdateArchivedReasonErrorComponent |
            ApiV1PrefixesUpdateCredentialIdErrorComponent | ApiV1PrefixesUpdateCriticalityErrorComponent |
            ApiV1PrefixesUpdateDebugModeErrorComponent | ApiV1PrefixesUpdateDescriptionErrorComponent |
            ApiV1PrefixesUpdateDisplayNameErrorComponent | ApiV1PrefixesUpdateKindErrorComponent |
            ApiV1PrefixesUpdateLabelsErrorComponent | ApiV1PrefixesUpdateNameErrorComponent |
            ApiV1PrefixesUpdateNonFieldErrorsErrorComponent | ApiV1PrefixesUpdateOrganizationIdErrorComponent |
            ApiV1PrefixesUpdatePlatformServiceErrorComponent | ApiV1PrefixesUpdateProviderEntityIdErrorComponent |
            ApiV1PrefixesUpdateProviderErrorComponent | ApiV1PrefixesUpdateProviderIdErrorComponent |
            ApiV1PrefixesUpdateProviderReferenceErrorComponent | ApiV1PrefixesUpdatePurposeErrorComponent |
            ApiV1PrefixesUpdateReconciliationEnabledErrorComponent | ApiV1PrefixesUpdateRegionIdErrorComponent |
            ApiV1PrefixesUpdateSlaAvailabilityErrorComponent | ApiV1PrefixesUpdateSlaTargetErrorComponent |
            ApiV1PrefixesUpdateSloAvailabilityErrorComponent | ApiV1PrefixesUpdateSloTargetErrorComponent |
            ApiV1PrefixesUpdateTargetAvailabilityErrorComponent | ApiV1PrefixesUpdateTolerationsErrorComponent |
            ApiV1PrefixesUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PrefixesUpdateAnnotationsErrorComponent
        | ApiV1PrefixesUpdateArchivedAtErrorComponent
        | ApiV1PrefixesUpdateArchivedErrorComponent
        | ApiV1PrefixesUpdateArchivedReasonErrorComponent
        | ApiV1PrefixesUpdateCredentialIdErrorComponent
        | ApiV1PrefixesUpdateCriticalityErrorComponent
        | ApiV1PrefixesUpdateDebugModeErrorComponent
        | ApiV1PrefixesUpdateDescriptionErrorComponent
        | ApiV1PrefixesUpdateDisplayNameErrorComponent
        | ApiV1PrefixesUpdateKindErrorComponent
        | ApiV1PrefixesUpdateLabelsErrorComponent
        | ApiV1PrefixesUpdateNameErrorComponent
        | ApiV1PrefixesUpdateNonFieldErrorsErrorComponent
        | ApiV1PrefixesUpdateOrganizationIdErrorComponent
        | ApiV1PrefixesUpdatePlatformServiceErrorComponent
        | ApiV1PrefixesUpdateProviderEntityIdErrorComponent
        | ApiV1PrefixesUpdateProviderErrorComponent
        | ApiV1PrefixesUpdateProviderIdErrorComponent
        | ApiV1PrefixesUpdateProviderReferenceErrorComponent
        | ApiV1PrefixesUpdatePurposeErrorComponent
        | ApiV1PrefixesUpdateReconciliationEnabledErrorComponent
        | ApiV1PrefixesUpdateRegionIdErrorComponent
        | ApiV1PrefixesUpdateSlaAvailabilityErrorComponent
        | ApiV1PrefixesUpdateSlaTargetErrorComponent
        | ApiV1PrefixesUpdateSloAvailabilityErrorComponent
        | ApiV1PrefixesUpdateSloTargetErrorComponent
        | ApiV1PrefixesUpdateTargetAvailabilityErrorComponent
        | ApiV1PrefixesUpdateTolerationsErrorComponent
        | ApiV1PrefixesUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_prefixes_update_annotations_error_component import (
            ApiV1PrefixesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_prefixes_update_archived_at_error_component import (
            ApiV1PrefixesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_prefixes_update_archived_error_component import ApiV1PrefixesUpdateArchivedErrorComponent
        from ..models.api_v1_prefixes_update_archived_reason_error_component import (
            ApiV1PrefixesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_prefixes_update_credential_id_error_component import (
            ApiV1PrefixesUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_criticality_error_component import (
            ApiV1PrefixesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_debug_mode_error_component import (
            ApiV1PrefixesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_prefixes_update_display_name_error_component import (
            ApiV1PrefixesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_prefixes_update_kind_error_component import ApiV1PrefixesUpdateKindErrorComponent
        from ..models.api_v1_prefixes_update_labels_error_component import ApiV1PrefixesUpdateLabelsErrorComponent
        from ..models.api_v1_prefixes_update_name_error_component import ApiV1PrefixesUpdateNameErrorComponent
        from ..models.api_v1_prefixes_update_non_field_errors_error_component import (
            ApiV1PrefixesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_prefixes_update_organization_id_error_component import (
            ApiV1PrefixesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_platform_service_error_component import (
            ApiV1PrefixesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_prefixes_update_provider_entity_id_error_component import (
            ApiV1PrefixesUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_provider_error_component import ApiV1PrefixesUpdateProviderErrorComponent
        from ..models.api_v1_prefixes_update_provider_id_error_component import (
            ApiV1PrefixesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_provider_reference_error_component import (
            ApiV1PrefixesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_prefixes_update_purpose_error_component import ApiV1PrefixesUpdatePurposeErrorComponent
        from ..models.api_v1_prefixes_update_reconciliation_enabled_error_component import (
            ApiV1PrefixesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_prefixes_update_region_id_error_component import ApiV1PrefixesUpdateRegionIdErrorComponent
        from ..models.api_v1_prefixes_update_sla_availability_error_component import (
            ApiV1PrefixesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_sla_target_error_component import (
            ApiV1PrefixesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_update_slo_availability_error_component import (
            ApiV1PrefixesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_slo_target_error_component import (
            ApiV1PrefixesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_update_target_availability_error_component import (
            ApiV1PrefixesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_tolerations_error_component import (
            ApiV1PrefixesUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_prefixes_update_workspace_id_error_component import (
            ApiV1PrefixesUpdateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PrefixesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateRegionIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesUpdatePurposeErrorComponent):
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
        from ..models.api_v1_prefixes_update_annotations_error_component import (
            ApiV1PrefixesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_prefixes_update_archived_at_error_component import (
            ApiV1PrefixesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_prefixes_update_archived_error_component import ApiV1PrefixesUpdateArchivedErrorComponent
        from ..models.api_v1_prefixes_update_archived_reason_error_component import (
            ApiV1PrefixesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_prefixes_update_credential_id_error_component import (
            ApiV1PrefixesUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_criticality_error_component import (
            ApiV1PrefixesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_debug_mode_error_component import (
            ApiV1PrefixesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_prefixes_update_description_error_component import (
            ApiV1PrefixesUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_prefixes_update_display_name_error_component import (
            ApiV1PrefixesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_prefixes_update_kind_error_component import ApiV1PrefixesUpdateKindErrorComponent
        from ..models.api_v1_prefixes_update_labels_error_component import ApiV1PrefixesUpdateLabelsErrorComponent
        from ..models.api_v1_prefixes_update_name_error_component import ApiV1PrefixesUpdateNameErrorComponent
        from ..models.api_v1_prefixes_update_non_field_errors_error_component import (
            ApiV1PrefixesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_prefixes_update_organization_id_error_component import (
            ApiV1PrefixesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_platform_service_error_component import (
            ApiV1PrefixesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_prefixes_update_provider_entity_id_error_component import (
            ApiV1PrefixesUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_provider_error_component import ApiV1PrefixesUpdateProviderErrorComponent
        from ..models.api_v1_prefixes_update_provider_id_error_component import (
            ApiV1PrefixesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_prefixes_update_provider_reference_error_component import (
            ApiV1PrefixesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_prefixes_update_purpose_error_component import ApiV1PrefixesUpdatePurposeErrorComponent
        from ..models.api_v1_prefixes_update_reconciliation_enabled_error_component import (
            ApiV1PrefixesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_prefixes_update_region_id_error_component import ApiV1PrefixesUpdateRegionIdErrorComponent
        from ..models.api_v1_prefixes_update_sla_availability_error_component import (
            ApiV1PrefixesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_sla_target_error_component import (
            ApiV1PrefixesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_update_slo_availability_error_component import (
            ApiV1PrefixesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_slo_target_error_component import (
            ApiV1PrefixesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_prefixes_update_target_availability_error_component import (
            ApiV1PrefixesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_prefixes_update_tolerations_error_component import (
            ApiV1PrefixesUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_prefixes_update_workspace_id_error_component import (
            ApiV1PrefixesUpdateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PrefixesUpdateAnnotationsErrorComponent
                | ApiV1PrefixesUpdateArchivedAtErrorComponent
                | ApiV1PrefixesUpdateArchivedErrorComponent
                | ApiV1PrefixesUpdateArchivedReasonErrorComponent
                | ApiV1PrefixesUpdateCredentialIdErrorComponent
                | ApiV1PrefixesUpdateCriticalityErrorComponent
                | ApiV1PrefixesUpdateDebugModeErrorComponent
                | ApiV1PrefixesUpdateDescriptionErrorComponent
                | ApiV1PrefixesUpdateDisplayNameErrorComponent
                | ApiV1PrefixesUpdateKindErrorComponent
                | ApiV1PrefixesUpdateLabelsErrorComponent
                | ApiV1PrefixesUpdateNameErrorComponent
                | ApiV1PrefixesUpdateNonFieldErrorsErrorComponent
                | ApiV1PrefixesUpdateOrganizationIdErrorComponent
                | ApiV1PrefixesUpdatePlatformServiceErrorComponent
                | ApiV1PrefixesUpdateProviderEntityIdErrorComponent
                | ApiV1PrefixesUpdateProviderErrorComponent
                | ApiV1PrefixesUpdateProviderIdErrorComponent
                | ApiV1PrefixesUpdateProviderReferenceErrorComponent
                | ApiV1PrefixesUpdatePurposeErrorComponent
                | ApiV1PrefixesUpdateReconciliationEnabledErrorComponent
                | ApiV1PrefixesUpdateRegionIdErrorComponent
                | ApiV1PrefixesUpdateSlaAvailabilityErrorComponent
                | ApiV1PrefixesUpdateSlaTargetErrorComponent
                | ApiV1PrefixesUpdateSloAvailabilityErrorComponent
                | ApiV1PrefixesUpdateSloTargetErrorComponent
                | ApiV1PrefixesUpdateTargetAvailabilityErrorComponent
                | ApiV1PrefixesUpdateTolerationsErrorComponent
                | ApiV1PrefixesUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_0 = (
                        ApiV1PrefixesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_1 = (
                        ApiV1PrefixesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_2 = (
                        ApiV1PrefixesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_3 = (
                        ApiV1PrefixesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_4 = (
                        ApiV1PrefixesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_5 = (
                        ApiV1PrefixesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_6 = (
                        ApiV1PrefixesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_7 = (
                        ApiV1PrefixesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_8 = (
                        ApiV1PrefixesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_9 = (
                        ApiV1PrefixesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_10 = (
                        ApiV1PrefixesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_11 = (
                        ApiV1PrefixesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_12 = (
                        ApiV1PrefixesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_13 = (
                        ApiV1PrefixesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_14 = (
                        ApiV1PrefixesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_15 = (
                        ApiV1PrefixesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_16 = (
                        ApiV1PrefixesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_17 = (
                        ApiV1PrefixesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_18 = (
                        ApiV1PrefixesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_19 = (
                        ApiV1PrefixesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_20 = (
                        ApiV1PrefixesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_21 = (
                        ApiV1PrefixesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_22 = (
                        ApiV1PrefixesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_23 = (
                        ApiV1PrefixesUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_24 = (
                        ApiV1PrefixesUpdateRegionIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_25 = (
                        ApiV1PrefixesUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_26 = (
                        ApiV1PrefixesUpdateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_update_error_type_27 = (
                        ApiV1PrefixesUpdatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_prefixes_update_error_type_28 = (
                    ApiV1PrefixesUpdateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_prefixes_update_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_prefixes_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_prefixes_update_validation_error.additional_properties = d
        return api_v1_prefixes_update_validation_error

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

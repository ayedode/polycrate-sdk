from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_prefixes_partial_update_annotations_error_component import (
        ApiV1PrefixesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_archived_at_error_component import (
        ApiV1PrefixesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_archived_error_component import (
        ApiV1PrefixesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_archived_reason_error_component import (
        ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_credential_id_error_component import (
        ApiV1PrefixesPartialUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_criticality_error_component import (
        ApiV1PrefixesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_debug_mode_error_component import (
        ApiV1PrefixesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_description_error_component import (
        ApiV1PrefixesPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_display_name_error_component import (
        ApiV1PrefixesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_kind_error_component import (
        ApiV1PrefixesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_labels_error_component import (
        ApiV1PrefixesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_name_error_component import (
        ApiV1PrefixesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_non_field_errors_error_component import (
        ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_organization_id_error_component import (
        ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_platform_service_error_component import (
        ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_provider_entity_id_error_component import (
        ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_provider_error_component import (
        ApiV1PrefixesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_provider_id_error_component import (
        ApiV1PrefixesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_provider_reference_error_component import (
        ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_purpose_error_component import (
        ApiV1PrefixesPartialUpdatePurposeErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_reconciliation_enabled_error_component import (
        ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_region_id_error_component import (
        ApiV1PrefixesPartialUpdateRegionIdErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_sla_availability_error_component import (
        ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_sla_target_error_component import (
        ApiV1PrefixesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_slo_availability_error_component import (
        ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_slo_target_error_component import (
        ApiV1PrefixesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_target_availability_error_component import (
        ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_tolerations_error_component import (
        ApiV1PrefixesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_prefixes_partial_update_workspace_id_error_component import (
        ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PrefixesPartialUpdateValidationError")


@_attrs_define
class ApiV1PrefixesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PrefixesPartialUpdateAnnotationsErrorComponent |
            ApiV1PrefixesPartialUpdateArchivedAtErrorComponent | ApiV1PrefixesPartialUpdateArchivedErrorComponent |
            ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent | ApiV1PrefixesPartialUpdateCredentialIdErrorComponent |
            ApiV1PrefixesPartialUpdateCriticalityErrorComponent | ApiV1PrefixesPartialUpdateDebugModeErrorComponent |
            ApiV1PrefixesPartialUpdateDescriptionErrorComponent | ApiV1PrefixesPartialUpdateDisplayNameErrorComponent |
            ApiV1PrefixesPartialUpdateKindErrorComponent | ApiV1PrefixesPartialUpdateLabelsErrorComponent |
            ApiV1PrefixesPartialUpdateNameErrorComponent | ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent | ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent
            | ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent | ApiV1PrefixesPartialUpdateProviderErrorComponent |
            ApiV1PrefixesPartialUpdateProviderIdErrorComponent | ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent |
            ApiV1PrefixesPartialUpdatePurposeErrorComponent | ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent
            | ApiV1PrefixesPartialUpdateRegionIdErrorComponent | ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PrefixesPartialUpdateSlaTargetErrorComponent | ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PrefixesPartialUpdateSloTargetErrorComponent | ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PrefixesPartialUpdateTolerationsErrorComponent | ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PrefixesPartialUpdateAnnotationsErrorComponent
        | ApiV1PrefixesPartialUpdateArchivedAtErrorComponent
        | ApiV1PrefixesPartialUpdateArchivedErrorComponent
        | ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent
        | ApiV1PrefixesPartialUpdateCredentialIdErrorComponent
        | ApiV1PrefixesPartialUpdateCriticalityErrorComponent
        | ApiV1PrefixesPartialUpdateDebugModeErrorComponent
        | ApiV1PrefixesPartialUpdateDescriptionErrorComponent
        | ApiV1PrefixesPartialUpdateDisplayNameErrorComponent
        | ApiV1PrefixesPartialUpdateKindErrorComponent
        | ApiV1PrefixesPartialUpdateLabelsErrorComponent
        | ApiV1PrefixesPartialUpdateNameErrorComponent
        | ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent
        | ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent
        | ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent
        | ApiV1PrefixesPartialUpdateProviderErrorComponent
        | ApiV1PrefixesPartialUpdateProviderIdErrorComponent
        | ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent
        | ApiV1PrefixesPartialUpdatePurposeErrorComponent
        | ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PrefixesPartialUpdateRegionIdErrorComponent
        | ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PrefixesPartialUpdateSlaTargetErrorComponent
        | ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PrefixesPartialUpdateSloTargetErrorComponent
        | ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PrefixesPartialUpdateTolerationsErrorComponent
        | ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_prefixes_partial_update_annotations_error_component import (
            ApiV1PrefixesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_archived_at_error_component import (
            ApiV1PrefixesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_archived_error_component import (
            ApiV1PrefixesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_archived_reason_error_component import (
            ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_credential_id_error_component import (
            ApiV1PrefixesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_criticality_error_component import (
            ApiV1PrefixesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_debug_mode_error_component import (
            ApiV1PrefixesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_display_name_error_component import (
            ApiV1PrefixesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_kind_error_component import (
            ApiV1PrefixesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_labels_error_component import (
            ApiV1PrefixesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_name_error_component import (
            ApiV1PrefixesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_non_field_errors_error_component import (
            ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_organization_id_error_component import (
            ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_platform_service_error_component import (
            ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_entity_id_error_component import (
            ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_error_component import (
            ApiV1PrefixesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_id_error_component import (
            ApiV1PrefixesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_reference_error_component import (
            ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_purpose_error_component import (
            ApiV1PrefixesPartialUpdatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_reconciliation_enabled_error_component import (
            ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_region_id_error_component import (
            ApiV1PrefixesPartialUpdateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_sla_availability_error_component import (
            ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_sla_target_error_component import (
            ApiV1PrefixesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_slo_availability_error_component import (
            ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_slo_target_error_component import (
            ApiV1PrefixesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_target_availability_error_component import (
            ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_tolerations_error_component import (
            ApiV1PrefixesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_workspace_id_error_component import (
            ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateRegionIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesPartialUpdatePurposeErrorComponent):
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
        from ..models.api_v1_prefixes_partial_update_annotations_error_component import (
            ApiV1PrefixesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_archived_at_error_component import (
            ApiV1PrefixesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_archived_error_component import (
            ApiV1PrefixesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_archived_reason_error_component import (
            ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_credential_id_error_component import (
            ApiV1PrefixesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_criticality_error_component import (
            ApiV1PrefixesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_debug_mode_error_component import (
            ApiV1PrefixesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_description_error_component import (
            ApiV1PrefixesPartialUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_display_name_error_component import (
            ApiV1PrefixesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_kind_error_component import (
            ApiV1PrefixesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_labels_error_component import (
            ApiV1PrefixesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_name_error_component import (
            ApiV1PrefixesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_non_field_errors_error_component import (
            ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_organization_id_error_component import (
            ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_platform_service_error_component import (
            ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_entity_id_error_component import (
            ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_error_component import (
            ApiV1PrefixesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_id_error_component import (
            ApiV1PrefixesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_provider_reference_error_component import (
            ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_purpose_error_component import (
            ApiV1PrefixesPartialUpdatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_reconciliation_enabled_error_component import (
            ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_region_id_error_component import (
            ApiV1PrefixesPartialUpdateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_sla_availability_error_component import (
            ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_sla_target_error_component import (
            ApiV1PrefixesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_slo_availability_error_component import (
            ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_slo_target_error_component import (
            ApiV1PrefixesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_target_availability_error_component import (
            ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_tolerations_error_component import (
            ApiV1PrefixesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_prefixes_partial_update_workspace_id_error_component import (
            ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PrefixesPartialUpdateAnnotationsErrorComponent
                | ApiV1PrefixesPartialUpdateArchivedAtErrorComponent
                | ApiV1PrefixesPartialUpdateArchivedErrorComponent
                | ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent
                | ApiV1PrefixesPartialUpdateCredentialIdErrorComponent
                | ApiV1PrefixesPartialUpdateCriticalityErrorComponent
                | ApiV1PrefixesPartialUpdateDebugModeErrorComponent
                | ApiV1PrefixesPartialUpdateDescriptionErrorComponent
                | ApiV1PrefixesPartialUpdateDisplayNameErrorComponent
                | ApiV1PrefixesPartialUpdateKindErrorComponent
                | ApiV1PrefixesPartialUpdateLabelsErrorComponent
                | ApiV1PrefixesPartialUpdateNameErrorComponent
                | ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent
                | ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent
                | ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent
                | ApiV1PrefixesPartialUpdateProviderErrorComponent
                | ApiV1PrefixesPartialUpdateProviderIdErrorComponent
                | ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent
                | ApiV1PrefixesPartialUpdatePurposeErrorComponent
                | ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PrefixesPartialUpdateRegionIdErrorComponent
                | ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PrefixesPartialUpdateSlaTargetErrorComponent
                | ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PrefixesPartialUpdateSloTargetErrorComponent
                | ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PrefixesPartialUpdateTolerationsErrorComponent
                | ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_0 = (
                        ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_1 = (
                        ApiV1PrefixesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_2 = (
                        ApiV1PrefixesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_3 = (
                        ApiV1PrefixesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_4 = (
                        ApiV1PrefixesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_5 = (
                        ApiV1PrefixesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_6 = (
                        ApiV1PrefixesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_7 = (
                        ApiV1PrefixesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_8 = (
                        ApiV1PrefixesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_9 = (
                        ApiV1PrefixesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_10 = (
                        ApiV1PrefixesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_11 = (
                        ApiV1PrefixesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_12 = (
                        ApiV1PrefixesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_13 = (
                        ApiV1PrefixesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_14 = (
                        ApiV1PrefixesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_15 = (
                        ApiV1PrefixesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_16 = (
                        ApiV1PrefixesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_17 = (
                        ApiV1PrefixesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_18 = (
                        ApiV1PrefixesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_19 = (
                        ApiV1PrefixesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_20 = (
                        ApiV1PrefixesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_21 = (
                        ApiV1PrefixesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_22 = (
                        ApiV1PrefixesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_23 = (
                        ApiV1PrefixesPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_24 = (
                        ApiV1PrefixesPartialUpdateRegionIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_25 = (
                        ApiV1PrefixesPartialUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_26 = (
                        ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_partial_update_error_type_27 = (
                        ApiV1PrefixesPartialUpdatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_prefixes_partial_update_error_type_28 = (
                    ApiV1PrefixesPartialUpdateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_prefixes_partial_update_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_prefixes_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_prefixes_partial_update_validation_error.additional_properties = d
        return api_v1_prefixes_partial_update_validation_error

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

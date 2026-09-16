from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertrouters_update_annotations_error_component import (
        ApiV1AlertroutersUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_archived_at_error_component import (
        ApiV1AlertroutersUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_archived_error_component import (
        ApiV1AlertroutersUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_archived_reason_error_component import (
        ApiV1AlertroutersUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_criticality_error_component import (
        ApiV1AlertroutersUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_debug_mode_error_component import (
        ApiV1AlertroutersUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_display_name_error_component import (
        ApiV1AlertroutersUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_kind_error_component import ApiV1AlertroutersUpdateKindErrorComponent
    from ..models.api_v1_alertrouters_update_label_cluster_error_component import (
        ApiV1AlertroutersUpdateLabelClusterErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_label_criticality_error_component import (
        ApiV1AlertroutersUpdateLabelCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_label_namespace_error_component import (
        ApiV1AlertroutersUpdateLabelNamespaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_label_organization_error_component import (
        ApiV1AlertroutersUpdateLabelOrganizationErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_label_pod_error_component import (
        ApiV1AlertroutersUpdateLabelPodErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_label_workspace_error_component import (
        ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_labels_error_component import ApiV1AlertroutersUpdateLabelsErrorComponent
    from ..models.api_v1_alertrouters_update_name_error_component import ApiV1AlertroutersUpdateNameErrorComponent
    from ..models.api_v1_alertrouters_update_non_field_errors_error_component import (
        ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_organization_id_error_component import (
        ApiV1AlertroutersUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_platform_service_error_component import (
        ApiV1AlertroutersUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_provider_error_component import (
        ApiV1AlertroutersUpdateProviderErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_provider_id_error_component import (
        ApiV1AlertroutersUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_provider_reference_error_component import (
        ApiV1AlertroutersUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_reconciliation_enabled_error_component import (
        ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_sla_availability_error_component import (
        ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_sla_target_error_component import (
        ApiV1AlertroutersUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_slo_availability_error_component import (
        ApiV1AlertroutersUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_slo_target_error_component import (
        ApiV1AlertroutersUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_target_availability_error_component import (
        ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_tolerations_error_component import (
        ApiV1AlertroutersUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_update_workspace_id_error_component import (
        ApiV1AlertroutersUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertroutersUpdateValidationError")


@_attrs_define
class ApiV1AlertroutersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertroutersUpdateAnnotationsErrorComponent | ApiV1AlertroutersUpdateArchivedAtErrorComponent
            | ApiV1AlertroutersUpdateArchivedErrorComponent | ApiV1AlertroutersUpdateArchivedReasonErrorComponent |
            ApiV1AlertroutersUpdateCriticalityErrorComponent | ApiV1AlertroutersUpdateDebugModeErrorComponent |
            ApiV1AlertroutersUpdateDisplayNameErrorComponent | ApiV1AlertroutersUpdateKindErrorComponent |
            ApiV1AlertroutersUpdateLabelClusterErrorComponent | ApiV1AlertroutersUpdateLabelCriticalityErrorComponent |
            ApiV1AlertroutersUpdateLabelNamespaceErrorComponent | ApiV1AlertroutersUpdateLabelOrganizationErrorComponent |
            ApiV1AlertroutersUpdateLabelPodErrorComponent | ApiV1AlertroutersUpdateLabelsErrorComponent |
            ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent | ApiV1AlertroutersUpdateNameErrorComponent |
            ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent | ApiV1AlertroutersUpdateOrganizationIdErrorComponent |
            ApiV1AlertroutersUpdatePlatformServiceErrorComponent | ApiV1AlertroutersUpdateProviderErrorComponent |
            ApiV1AlertroutersUpdateProviderIdErrorComponent | ApiV1AlertroutersUpdateProviderReferenceErrorComponent |
            ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent |
            ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent | ApiV1AlertroutersUpdateSlaTargetErrorComponent |
            ApiV1AlertroutersUpdateSloAvailabilityErrorComponent | ApiV1AlertroutersUpdateSloTargetErrorComponent |
            ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent | ApiV1AlertroutersUpdateTolerationsErrorComponent |
            ApiV1AlertroutersUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertroutersUpdateAnnotationsErrorComponent
        | ApiV1AlertroutersUpdateArchivedAtErrorComponent
        | ApiV1AlertroutersUpdateArchivedErrorComponent
        | ApiV1AlertroutersUpdateArchivedReasonErrorComponent
        | ApiV1AlertroutersUpdateCriticalityErrorComponent
        | ApiV1AlertroutersUpdateDebugModeErrorComponent
        | ApiV1AlertroutersUpdateDisplayNameErrorComponent
        | ApiV1AlertroutersUpdateKindErrorComponent
        | ApiV1AlertroutersUpdateLabelClusterErrorComponent
        | ApiV1AlertroutersUpdateLabelCriticalityErrorComponent
        | ApiV1AlertroutersUpdateLabelNamespaceErrorComponent
        | ApiV1AlertroutersUpdateLabelOrganizationErrorComponent
        | ApiV1AlertroutersUpdateLabelPodErrorComponent
        | ApiV1AlertroutersUpdateLabelsErrorComponent
        | ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent
        | ApiV1AlertroutersUpdateNameErrorComponent
        | ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent
        | ApiV1AlertroutersUpdateOrganizationIdErrorComponent
        | ApiV1AlertroutersUpdatePlatformServiceErrorComponent
        | ApiV1AlertroutersUpdateProviderErrorComponent
        | ApiV1AlertroutersUpdateProviderIdErrorComponent
        | ApiV1AlertroutersUpdateProviderReferenceErrorComponent
        | ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent
        | ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent
        | ApiV1AlertroutersUpdateSlaTargetErrorComponent
        | ApiV1AlertroutersUpdateSloAvailabilityErrorComponent
        | ApiV1AlertroutersUpdateSloTargetErrorComponent
        | ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent
        | ApiV1AlertroutersUpdateTolerationsErrorComponent
        | ApiV1AlertroutersUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertrouters_update_annotations_error_component import (
            ApiV1AlertroutersUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_archived_at_error_component import (
            ApiV1AlertroutersUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_archived_error_component import (
            ApiV1AlertroutersUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_archived_reason_error_component import (
            ApiV1AlertroutersUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_criticality_error_component import (
            ApiV1AlertroutersUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_debug_mode_error_component import (
            ApiV1AlertroutersUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_display_name_error_component import (
            ApiV1AlertroutersUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_kind_error_component import (
            ApiV1AlertroutersUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_cluster_error_component import (
            ApiV1AlertroutersUpdateLabelClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_namespace_error_component import (
            ApiV1AlertroutersUpdateLabelNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_organization_error_component import (
            ApiV1AlertroutersUpdateLabelOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_pod_error_component import (
            ApiV1AlertroutersUpdateLabelPodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_workspace_error_component import (
            ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_labels_error_component import (
            ApiV1AlertroutersUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_name_error_component import (
            ApiV1AlertroutersUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_non_field_errors_error_component import (
            ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_organization_id_error_component import (
            ApiV1AlertroutersUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_platform_service_error_component import (
            ApiV1AlertroutersUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_provider_error_component import (
            ApiV1AlertroutersUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_provider_id_error_component import (
            ApiV1AlertroutersUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_provider_reference_error_component import (
            ApiV1AlertroutersUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_reconciliation_enabled_error_component import (
            ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_sla_availability_error_component import (
            ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_sla_target_error_component import (
            ApiV1AlertroutersUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_slo_availability_error_component import (
            ApiV1AlertroutersUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_slo_target_error_component import (
            ApiV1AlertroutersUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_target_availability_error_component import (
            ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_tolerations_error_component import (
            ApiV1AlertroutersUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_workspace_id_error_component import (
            ApiV1AlertroutersUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateLabelOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateLabelClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateLabelPodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersUpdateLabelNamespaceErrorComponent):
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
        from ..models.api_v1_alertrouters_update_annotations_error_component import (
            ApiV1AlertroutersUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_archived_at_error_component import (
            ApiV1AlertroutersUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_archived_error_component import (
            ApiV1AlertroutersUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_archived_reason_error_component import (
            ApiV1AlertroutersUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_criticality_error_component import (
            ApiV1AlertroutersUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_debug_mode_error_component import (
            ApiV1AlertroutersUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_display_name_error_component import (
            ApiV1AlertroutersUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_kind_error_component import (
            ApiV1AlertroutersUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_cluster_error_component import (
            ApiV1AlertroutersUpdateLabelClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_criticality_error_component import (
            ApiV1AlertroutersUpdateLabelCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_namespace_error_component import (
            ApiV1AlertroutersUpdateLabelNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_organization_error_component import (
            ApiV1AlertroutersUpdateLabelOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_pod_error_component import (
            ApiV1AlertroutersUpdateLabelPodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_label_workspace_error_component import (
            ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_labels_error_component import (
            ApiV1AlertroutersUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_name_error_component import (
            ApiV1AlertroutersUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_non_field_errors_error_component import (
            ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_organization_id_error_component import (
            ApiV1AlertroutersUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_platform_service_error_component import (
            ApiV1AlertroutersUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_provider_error_component import (
            ApiV1AlertroutersUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_provider_id_error_component import (
            ApiV1AlertroutersUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_provider_reference_error_component import (
            ApiV1AlertroutersUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_reconciliation_enabled_error_component import (
            ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_sla_availability_error_component import (
            ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_sla_target_error_component import (
            ApiV1AlertroutersUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_slo_availability_error_component import (
            ApiV1AlertroutersUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_slo_target_error_component import (
            ApiV1AlertroutersUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_target_availability_error_component import (
            ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_tolerations_error_component import (
            ApiV1AlertroutersUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_update_workspace_id_error_component import (
            ApiV1AlertroutersUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertroutersUpdateAnnotationsErrorComponent
                | ApiV1AlertroutersUpdateArchivedAtErrorComponent
                | ApiV1AlertroutersUpdateArchivedErrorComponent
                | ApiV1AlertroutersUpdateArchivedReasonErrorComponent
                | ApiV1AlertroutersUpdateCriticalityErrorComponent
                | ApiV1AlertroutersUpdateDebugModeErrorComponent
                | ApiV1AlertroutersUpdateDisplayNameErrorComponent
                | ApiV1AlertroutersUpdateKindErrorComponent
                | ApiV1AlertroutersUpdateLabelClusterErrorComponent
                | ApiV1AlertroutersUpdateLabelCriticalityErrorComponent
                | ApiV1AlertroutersUpdateLabelNamespaceErrorComponent
                | ApiV1AlertroutersUpdateLabelOrganizationErrorComponent
                | ApiV1AlertroutersUpdateLabelPodErrorComponent
                | ApiV1AlertroutersUpdateLabelsErrorComponent
                | ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent
                | ApiV1AlertroutersUpdateNameErrorComponent
                | ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent
                | ApiV1AlertroutersUpdateOrganizationIdErrorComponent
                | ApiV1AlertroutersUpdatePlatformServiceErrorComponent
                | ApiV1AlertroutersUpdateProviderErrorComponent
                | ApiV1AlertroutersUpdateProviderIdErrorComponent
                | ApiV1AlertroutersUpdateProviderReferenceErrorComponent
                | ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent
                | ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent
                | ApiV1AlertroutersUpdateSlaTargetErrorComponent
                | ApiV1AlertroutersUpdateSloAvailabilityErrorComponent
                | ApiV1AlertroutersUpdateSloTargetErrorComponent
                | ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent
                | ApiV1AlertroutersUpdateTolerationsErrorComponent
                | ApiV1AlertroutersUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_0 = (
                        ApiV1AlertroutersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_1 = (
                        ApiV1AlertroutersUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_2 = (
                        ApiV1AlertroutersUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_3 = (
                        ApiV1AlertroutersUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_4 = (
                        ApiV1AlertroutersUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_5 = (
                        ApiV1AlertroutersUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_6 = (
                        ApiV1AlertroutersUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_7 = (
                        ApiV1AlertroutersUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_8 = (
                        ApiV1AlertroutersUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_9 = (
                        ApiV1AlertroutersUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_10 = (
                        ApiV1AlertroutersUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_11 = (
                        ApiV1AlertroutersUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_12 = (
                        ApiV1AlertroutersUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_13 = (
                        ApiV1AlertroutersUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_14 = (
                        ApiV1AlertroutersUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_15 = (
                        ApiV1AlertroutersUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_16 = (
                        ApiV1AlertroutersUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_17 = (
                        ApiV1AlertroutersUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_18 = (
                        ApiV1AlertroutersUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_19 = (
                        ApiV1AlertroutersUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_20 = (
                        ApiV1AlertroutersUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_21 = (
                        ApiV1AlertroutersUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_22 = (
                        ApiV1AlertroutersUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_23 = (
                        ApiV1AlertroutersUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_24 = (
                        ApiV1AlertroutersUpdateLabelWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_25 = (
                        ApiV1AlertroutersUpdateLabelOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_26 = (
                        ApiV1AlertroutersUpdateLabelClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_27 = (
                        ApiV1AlertroutersUpdateLabelPodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_update_error_type_28 = (
                        ApiV1AlertroutersUpdateLabelNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertrouters_update_error_type_29 = (
                    ApiV1AlertroutersUpdateLabelCriticalityErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertrouters_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertrouters_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertrouters_update_validation_error.additional_properties = d
        return api_v1_alertrouters_update_validation_error

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
